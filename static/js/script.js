/* Disable +/- buttons outside 1-50 range */

function handleEnableDisable(productSku) {
    var currentValue = parseInt($(`.sku_qty_${productSku}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 49;

    $(`.decrement-qty_${productSku}`).prop('disabled', minusDisabled);
    $(`.increment-qty_${productSku}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
var allQtyInputs = $('.qty_input');
for(var i = 0; i < allQtyInputs.length; i++){
    var productSku = $(allQtyInputs[i]).data('product_sku');
    handleEnableDisable(productSku);
}

// Check enable/disable every time the input is changed
$('.qty_input').change(function() {
    var productSku = $(this).data('product_sku');
    handleEnableDisable(productSku);
});

// Increment quantity
$('.increment-qty').click(function(e) {
   e.preventDefault();
   var productSku = $(this).data('product_sku');
   var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
   var allQuantityInputs = $(`.input-group-${productSku} input[name='quantity']`);
   var currentValue = parseInt($(closestInput).val());
   $(allQuantityInputs).val(currentValue + 1);
   handleEnableDisable(productSku);
});

// Decrement quantity
$('.decrement-qty').click(function(e) {
    e.preventDefault();
    var productSku = $(this).data('product_sku');
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var allQuantityInputs = $(`.input-group-${productSku} input[name='quantity']`);
    var currentValue = parseInt($(closestInput).val());
    $(allQuantityInputs).val(currentValue - 1);
    handleEnableDisable(productSku);
 });

 // Update quantity on click
 $('.update-link').click(function(e) {
    var form = $(this).parent().prev().children('.update-form');
    form.submit();
});

// Show toast messages
$('.toast').toast('show');

