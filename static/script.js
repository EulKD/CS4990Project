const formElem = document.querySelector("form");

const display = document.querySelector("#display");


/**
 * This function is an event listener for form submission.
 * It prevents the default form submission and creates a new FormData object.
 * 
 * @param {Event} e - The event object.
 */
formElem.addEventListener("submit", (e) => {
  // on form submission, prevent default
  e.preventDefault();

  // construct a FormData object, which fires the formdata event
  new FormData(formElem);
});

/**
 * Event listener for the 'formdata' event on the form element.
 * This event is fired after the form data has been constructed, but before the form is submitted.
 * 
 * @param {Event} e - The event object.
 */
formElem.addEventListener("formdata", (e) => {
  console.log("formdata fired");

  /**
   * Extract the form data from the event object.
   * 
   * @type {string} serving_size - The serving size from the form data.
   * @type {string} diet_details - The diet details from the form data.
   * @type {string} budget - The budget from the form data.
   */
  const serving_size = e.formData.get("serving_size");
  const diet_details = e.formData.get("diet_details");
  const budget = e.formData.get("budget");

  console.log(serving_size, diet_details, budget);
  console.log(JSON.stringify({ serving_size, diet_details, budget }))

  /**
   * Submit the form data to the server using the fetch API.
   * Generate the grocery shopping list using serving_size, diet_details, and budget as parameters.
   * The server is expected to respond with JSON data.
   */
  fetch("http://127.0.0.1:5000/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ serving_size, diet_details, budget }),
  })
    .then((response) => response.json())
    .then((data) => {
        console.log(data)
        display.innerHTML = data;
    })
});
