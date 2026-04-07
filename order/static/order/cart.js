const menuItems = document.getElementsByClassName("menu-item")
const cartCount = document.getElementById("cart-count")
const cartTotal = document.getElementById("cart-total")
const cartForm = document.getElementById("cart-form")

let total = 0
let count = 0
let cart = {}

for (let i = 0; i < menuItems.length; i++) {
    const menuItem = menuItems[i];
    const slug = menuItem.dataset.slug
    const price = parseFloat(menuItem.dataset.price)
    const addButton = menuItem.querySelector(".add-button")
    const clearButton = menuItem.querySelector(".clear-button")
    
    addButton.addEventListener("click", () => {
        total += price
        count += 1
        
        if (menuItem.dataset.slug in cart)
            cart[slug] += 1
        else
            cart[slug] = 1

        addButton.textContent = "ADD | " + cart[slug]
        clearButton.style.display = "inline"

        cartCount.textContent = count
        cartTotal.textContent = total
        console.log(cart, total)
    })

    clearButton.addEventListener("click", () => {
        total -= cart[slug] * price
        count -= cart[slug]
        delete cart[slug]

        addButton.textContent = "ADD"
        clearButton.style.display = "none"

        cartCount.textContent = count
        cartTotal.textContent = total
        console.log(cart, total)
    })
}

cartForm.addEventListener("submit", (event) => {
    event.preventDefault();

    if (Object.keys(cart).length > 0) {
        document.getElementById("cart-data").value = JSON.stringify(cart)
        cartForm.submit();
    }
})