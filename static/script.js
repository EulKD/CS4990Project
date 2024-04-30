const formElem = document.querySelector("form");

const dishElem = document.getElementById('dish');
const servingsElem = document.getElementById('servings');
const shopElem = document.getElementById('shopping_list');
const costElem = document.getElementById('cost');
const recipeElem = document.getElementById('recipe');
const suggestElem = document.getElementById('suggestions');

// --------------form event listener and FormData obj----------
formElem.addEventListener("submit", (e) => {
  // on form submission, prevent default
  e.preventDefault();

  // construct a FormData object, which fires the formdata event
  new FormData(formElem);
});


// --------------event listener for form data----------
formElem.addEventListener("formdata", (e) => {
  console.log("formdata fired");

  // --------------extract form data----------
  const serving_size = e.formData.get("serving_size");
  const diet_details = e.formData.get("diet_details");
  const budget = e.formData.get("budget");

  console.log(serving_size, diet_details, budget);
  console.log(JSON.stringify({ serving_size, diet_details, budget }))

  // --------------submit form data and generate JSON data response----------
  fetch("http://127.0.0.1:5000/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ serving_size, diet_details, budget }),
  })
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        section(data);
    })
});

// --------------split data into different sections----------
function section(data) {
  const sections = data.split('---');
  console.log(sections)

  const dish = sections[0].trim();
  dishElem.innerText = dish;
  console.log(dish)

  const servings = sections[1].trim();
  servingsElem.innerHTML = servings;

  const shop = sections[2].trim();
  shopElem.innerText = shop;

  const cost = sections[3].trim();
  costElem.innerHTML = cost;

  const recipe = sections[4].trim();
  recipeElem.innerHTML = recipe;

  const suggest = sections[5].trim();
  suggestElem.innerHTML = suggest;
}

// ---------vertical-menu with-inner-menu-active-animation-----------

var tabsVerticalInner = $('#accordian');
var selectorVerticalInner = $('#accordian').find('li').length;
var activeItemVerticalInner = tabsVerticalInner.find('.active');
var activeWidthVerticalHeight = activeItemVerticalInner.innerHeight();
var activeWidthVerticalWidth = activeItemVerticalInner.innerWidth();
var itemPosVerticalTop = activeItemVerticalInner.position();
var itemPosVerticalLeft = activeItemVerticalInner.position();
$(".selector-active").css({
	"top":itemPosVerticalTop.top + "px", 
	"left":itemPosVerticalLeft.left + "px",
	"height": activeWidthVerticalHeight + "px",
	"width": activeWidthVerticalWidth + "px"
});
$("#accordian").on("click","li",function(e){
	$('#accordian ul li').removeClass("active");
	$(this).addClass('active');
	var activeWidthVerticalHeight = $(this).innerHeight();
	var activeWidthVerticalWidth = $(this).innerWidth();
	var itemPosVerticalTop = $(this).position();
	var itemPosVerticalLeft = $(this).position();
	$(".selector-active").css({
		"top":itemPosVerticalTop.top + "px", 
		"left":itemPosVerticalLeft.left + "px",
		"height": activeWidthVerticalHeight + "px",
		"width": activeWidthVerticalWidth + "px"
	});
});


// --------------add active class-on another-page move----------
jQuery(document).ready(function($){
  // Get current path and find target link
  var path = window.location.pathname.split("/").pop();

  // Account for home page with empty path
  if ( path == '' ) {
    path = 'plan';
  }

  var target = $('#accordian ul li a[href="'+path+'"]');
  // Add active class to target link
  target.parent().addClass('active');
});
