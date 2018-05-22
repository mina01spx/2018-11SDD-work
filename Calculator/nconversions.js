/* When the input field receives input, convert the value from feet to meters */
function lengthConverter(valNum) {
  document.getElementById("outputMeters").innerHTML = valNum / 0.0022046;
}