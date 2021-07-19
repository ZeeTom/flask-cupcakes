"use strict";

const BASE_URL = "http://localhost:5000/api/cupcakes";
const $cupcakeList = $("#cupcake-list");
const $submit = $("#submit");
const $flavor = $("#flavor");
const $size = $("#size");
const $rating = $("#rating");
const $image = $("#image");
// prevent default on event listener
// TODO: Think of better name
async function showCupcakes() {
  let response = await axios.get(BASE_URL);
  let cupcakes = response.data.cupcakes;

  $cupcakeList.empty();
  addCupcakesToDOM(cupcakes);
}

async function addCupcake(e) {
  e.preventDefault();

  let flavor = $flavor.val();
  console.log(flavor);
  let size = $size.val();
  let rating = $rating.val();
  let image = $image.val();

  let cupcake = { flavor, size, rating, image };

  // TODO: separate functions

  await axios.post(BASE_URL, cupcake);
  await showCupcakes();
}

function addCupcakesToDOM(cupcakes) {
  for (let cupcake of cupcakes) {
    let $cupcake = $(
      `<li>${cupcake.flavor} ${cupcake.size} ${cupcake.rating} <img src='${cupcake.image}'></li>`
    );

    $cupcakeList.append($cupcake);
  }
}

$(showCupcakes);

$submit.on("click", addCupcake);
