(function () {
    function render($el, value) {
        value = value ? 1 : "";
        var text = "";
        var data = $el.data('source');
        $el.data('value', value);
        for (var k in data) {
            var entry = data[k];
            if (entry['value'] == value) {
                text = " " + entry['text'];
            }
        }
        if (value === 1) {
            $el.html('<span class="fa fa-check-circle glyphicon glyphicon-ok-circle icon-ok-circle"></span>' + text);
        } else {
            $el.html('<span class="fa fa-minus-circle glyphicon glyphicon-minus-sign icon-minus-sign"></span>' + text);
        }
    }

    function valueFromHtml($el) {
        return $el.data('value') == 1;
    }

    function onClick(e) {
        var $el = $(e.target);
        var params = {};
        var value = !valueFromHtml($el);
        params['list_form_pk'] = $el.data('pk');
        params[$el.attr('name')] = value ? 1 : "";
        if ($el.data('csrf')) {
            params['csrf_token'] = $el.data('csrf');
        }
        $.ajax({
            type: "POST",
            url: $el.data('url'),
            data: params,
            success: function (data, status) {
                if (status === "success") {
                    render($el, value);
                } else {
                    alert("Query error: " + (data || message));
                }
            },
            error: function (xhr, message) {
                alert("Query error: " + (xhr.responseText || message));
            }
        });
    }

    function applyToggleControl($el) {
        render($el, valueFromHtml($el));
        $el.click(onClick);
    }

    $('[data-role=toggle-control]').each(function () {
        applyToggleControl($(this));
    });
})();
