const userInput = require("./userInput");
const simplePost = require("./simplePost");

/* Create an outer main function allowing us to adhere to the rule that
all await calls must appear within an async function.
*/
async function main() {
  // Call our pre-prepared functions in order to get use input.
  userInput.startInput();
  // Remember to await in order to allow for input that may take a variable amount of time.
  let location = await userInput.getInput("Enter a location: ");
  let days = await userInput.getInput("Days from now: ");
  // Pre-construct body, just for neatness.
  // We're adhering to the structure expected by the server.
  // Note that we have to enclose all strings, even the values in speech marks. Didn't need to do this with pythagoras.
  let body = "{\"location\":\"" + location + "\", \"days\":" + days + "}";
  // Pass everything as a key/value dictionary, as dictated by the method.
  // Again we await.
  // Open question: how would we test this?
  weather = await simplePost.httpPostJSON({
    body: body,
    hostname: "localhost",
    port: 8888
  });
  // Note different way of printing.
  console.log(weather);
  // Stop waiting for input, so that the program ends.
  userInput.endInput();
}

main();
