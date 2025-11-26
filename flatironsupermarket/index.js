
const items = ["Sugar", "cabbage", "salt",]

function itemToPurchase(itemToPurchase, quantity){
    if(!items.includes(itemToPurchase)){
        console.log("error: Invalid item! unable to complete purchase")
        return
    } if( isNaN(quantity)){
        console("error: Invalid quantity! Unable to complete purchase")
    }

let price
if (itemToPurchase === "sugar"){
    price = 1.99}
if (itemToPurchase === "cabbage"){
    price = 0.99}
else if (itemToPurchase === "salt"){
    price = 2.99}
const totalPrice = price * quantity
console.log(
    `Thank you for buying with us. You have bought ${quantity} units of  ${itemToPurchase} The total price is ${totalPrice}`
)}
function addNewItem(newItem){
    items.push(newItem)
    console.log(`${newItem} succesfully added to the supermarket`)
}




console.log("Welcome to FlatironSupermarket!")
itemToPurchase("rice", 3)
itemToPurchase("cabbage", 2)
itemToPurchase("sugar", 6)
addNewItem("pineapple")

    