async function runCommand() {
  const cmd = document.getElementById("cmd").value;

  // ❌ no validation
  const res = await fetch(`http://localhost:8000/run?cmd=${cmd}`);
  const data = await res.json();

  console.log(data);
}