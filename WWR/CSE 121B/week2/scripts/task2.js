//VARIABLES

// Step 1

const myName = "Jonathan Ricardo";
//Step 2
document.querySelector('#name').textContent = myName;

//Step 3
const currentYear = 2023;

//Step 4
document.querySelector('#year').textContent = currentYear;

//Step 5
const myPicture = 'images/pic.jpeg';

//Step 6
//Picture added

//Step 7
document.querySelector('img').setAttribute('src', myPicture);

//....................................................

//ARRAYS

//Step 1
let favoriteFoods = ('Sushi', 'Hot Dog', 'Pizza');

//Step 2
document.querySelector('#food').textContent = favoriteFoods;

//Step 3
let anotherFavoriteFood = ['Fried Chicken'];

//Step 4
favoriteFoods.push(anotherFavoriteFood);

//Step 5
document.querySelector('#food').textContent = favoriteFoods;

//Step 6
favoriteFoods.shift();

//Step 7
document.querySelector('#food').textContent = favoriteFoods;


//Step 8
favoriteFoods.pop();

//Step 9
document.querySelector('#food').textContent = favoriteFoods