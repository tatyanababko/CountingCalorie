/*
 * Bootstrap modal：2016-12-17 updated
 * Modal can be customized by 'defaultAtrributes'
 * 'ajaxSubmitSuccess' event can be used to write custom callback
 * Events:
 * - close modal，add 'data-dismiss="modal"' on a trigger element
 * - submit form use ajax，add 'data-submit="modal"' on a trigger element
 * Multiple modal instance supported, different task is better to use different modal instance
 */
function Dialog(attributes) {
    var defaultAtrributes = {
        width: "600px",
        height: "auto",
        titleText: "Title",
        content: "",
        confirmBtnText: "Confirm",
        cancelBtnText: "Cancel",
        showFooter: true,
        triggerEle: "" // jquery selector
    }

    $.extend(this, defaultAtrributes, attributes)

    // get trigger element's jQuery object
    if (this.triggerEle) {
        this.triggerEle = $(this.triggerEle)
    }

    // initialize modal structure and layout
    this._initView()

    // bind modal event callback
    this._initController()
}

$.extend(Dialog.prototype, {
    _initView: function () {
        var $modalBackdrop = $('.modal-backdrop')

        this.$body = $('body')

        // parse modal template, insert data from defaultAttributes
        this.$element = $(this._build(this._getDoc(this._dialogTpl), this))

        // insert content
        this.$element.find('.modal-body').html(this.content)

        if(!this.showFooter) {
            this.$element.find('.modal-footer').remove()
        }

        if ($modalBackdrop.length) {
            this.$maskEle = $modalBackdrop
        } else {
            this.$maskEle = $('<div class="modal-backdrop fade" style="display: none;"></div>')
        }

        this.$body
            .append(this.$element)
            .append(this.$maskEle)

        /* make modal support event by using jQuery events
         * 如果使用 Dialog.prototype.on = this._switchThis(this.$element.on, this.$element)
         * 则每个实例将直接重写原型，组件就不能支持需要使用多个实例的场景。
         */
        this.on = this._switchThis(this.$element.on, this.$element)
        this.trigger = this._switchThis(this.$element.trigger, this.$element)
    },
    _initController: function () {
        if(this.triggerEle) {
            var _this = this;
            this.triggerEle.on('click', function() {
                _this.show()
            })
        }

        this.$element.on('click', '[data-dismiss="modal"]', this._switchThis(this.close, this))
        this.$element.on('click', '[data-submit="modal"]', this._switchThis(this.ajaxSubmit, this))
    },
    _switchThis: function (fn, obj) {
        return function () {
            fn.apply(obj, arguments)
        }
    },
    _getDoc: function (fn) {
        return fn.toString()
            .replace(/^[^\/]+\/\*!?/, '')
            .replace(/\*\/[^\/]+$/, '')
            .replace(/^[\s\xA0]+/, '')
            .replace(/[\s\xA0]+$/, '')
    },
    _build: function(doc, data) {
        return doc.replace(/{{(\w+)}}/g, function(match, index) {
            return data[index] || ''
        })
    },
    _adjustDialog: function () { // borrow from bootstrap
        var modalIsOverflowing = this.$element[0].scrollHeight > document.documentElement.clientHeight

        this.$element.css({
            paddingLeft:  !this.bodyIsOverflowing && modalIsOverflowing ? this.scrollbarWidth : '',
            paddingRight: this.bodyIsOverflowing && !modalIsOverflowing ? this.scrollbarWidth : ''
        })
    },
    _resetAdjustments: function () { // borrow from bootstrap
        this.$element.css({
            paddingLeft: '',
            paddingRight: ''
        })
    },
    _checkScrollbar: function () { // borrow from bootstrap
        var fullWindowWidth = window.innerWidth
        if (!fullWindowWidth) { // workaround for missing window.innerWidth in IE8
            var documentElementRect = document.documentElement.getBoundingClientRect()
            fullWindowWidth = documentElementRect.right - Math.abs(documentElementRect.left)
        }
        this.bodyIsOverflowing = document.body.clientWidth < fullWindowWidth
        this.scrollbarWidth = this._measureScrollbar()
    },
    _setScrollbar: function () { // borrow from bootstrap
      var bodyPad = parseInt((this.$body.css('padding-right') || 0), 10)
      this.originalBodyPad = document.body.style.paddingRight || ''
      if (this.bodyIsOverflowing) this.$body.css('padding-right', bodyPad + this.scrollbarWidth)
    },
    _resetScrollbar: function () { // borrow from bootstrap
        this.$body.css('padding-right', this.originalBodyPad)
    },
    _measureScrollbar: function () { // borrow from bootstrap
      var scrollDiv = document.createElement('div')
      scrollDiv.className = 'modal-scrollbar-measure'
      this.$body.append(scrollDiv)
      var scrollbarWidth = scrollDiv.offsetWidth - scrollDiv.clientWidth
      this.$body[0].removeChild(scrollDiv)
      return scrollbarWidth
    },
    close: function() {
        this._resetAdjustments()
        this._resetScrollbar()

        this.$body.removeClass('modal-open');
        this.$element
            .hide()
            .removeClass('in')
        this.$maskEle
            .hide()
            .removeClass('in')
    },
    show: function() {
        var _this = this

        this._checkScrollbar()
        this._setScrollbar()

        // use .modal-open to prevent default scrolling behavior
        this.$body.addClass('modal-open')

        this.$element.show().scrollTop(0)
        this.$maskEle.show()

        this._adjustDialog()

        setTimeout(function() {
            _this.$maskEle.addClass('in')
            _this.$element.addClass('in')
        })
    },
    ajaxSubmit: function(event, data) {
        var that = this,
           $form = that.$element.find('form'),
          $alert = $form.find('.alert'),
             url = $form.attr('action'),
             meth = $form.attr('method'),
        submitData = data ? data : $form.serializeArray();

        $.ajax({
            url: url,
            data: submitData,
            method: meth ? meth : 'post',
            dataType: 'json',
            cache: false
        }).done(function(data) {
            if(data.success === true) {
                that.close()
                that.trigger('ajaxSubmitSuccess')
            } else {
                if ($alert.length) {
                    $alert.html(data.message).show()
                } else {
                    $form.prepend($('<div class="alert alert-danger" role="alert">'+ data.message +'</div>'))
                }
            }
        }).fail(function() {
            if ($alert.length) {
                $alert.html('Error').show()
            } else {
                $form.prepend($('<div class="alert alert-danger" role="alert">Error</div>'))
            }
        })
    },
    resetDialogTitle: function(content) {
        this.$element.find('.modal-title').html(content);
        return this
    },
    insertDialogContent: function(content) {
        this.$element.find('.modal-body').html(content)
        return this
    },
    resetDialogFooter: function(content) {
        this.$element.find('.modal-footer').html(content);
        return this
    },
    resetCancelBtnText: function(content) {
        this.$element.find('.modal-footer [data-dismiss="modal"]').html(content);
        return this
    },
    resetConfirmBtnText: function(content) {
        this.$element.find('.modal-footer [data-submit="modal"]').html(content);
        return this
    },
    _dialogTpl: function() {
      /*!
      <div class="modal fade">
        <div class="modal-dialog" style="width: {{width}}; height: {{height}};">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal"><span>&times;</span></button>
                    <h4 class="modal-title">{{titleText}}</h4>
                </div>

                <!-- body start -->
                <div class="modal-body"></div>
                <!-- /body end -->

                <!-- footer start -->
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">{{cancelBtnText}}</button>
                    <button type="button" class="btn btn-primary" data-submit="modal">{{confirmBtnText}}</button>
                </div>
                <!-- /footer end -->
            </div>
        </div>
      </div>
      */
    }
})