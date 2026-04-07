const orderItems = document.getElementsByClassName("order-item")
const orderForm = document.getElementById("order-form")
const orderTotal = document.getElementById("order-total")
const restaurantSlug = document.getElementById("restaurant-heading").dataset.restaurant
const cart = {};
let total = 0;

for (let i = 0; i < orderItems.length; i++) {
    const orderItem = orderItems[i];
    cart[orderItem.dataset.slug] = orderItem.dataset.quantity;
    total += parseFloat(orderItem.dataset.price) * orderItem.dataset.quantity;
}

orderTotal.innerText = total;

orderForm.addEventListener("submit", (event) => {
    event.preventDefault();

    if (Object.keys(cart).length > 0) {
        document.getElementById("order-restaurant").value = restaurantSlug
        document.getElementById("order-data").value = JSON.stringify(cart)
        orderForm.submit();
    }
})