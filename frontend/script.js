const API_URL = "http://127.0.0.1:8000";

// Fetch and render all deployments
async function fetchDeployments() {
  const res = await fetch(`${API_URL}/deployments`);
  const deployments = await res.json();
  renderDeployments(deployments);
}

// Render deployments table
function renderDeployments(deployments) {
  const tableBody = document.getElementById("deployments-body");
  tableBody.innerHTML = "";

  deployments.forEach(d => {
    const row = document.createElement("tr");

    // Name
    const nameCell = document.createElement("td");
    nameCell.textContent = d.name;
    row.appendChild(nameCell);

    // State with color
    const stateCell = document.createElement("td");
    stateCell.textContent = d.state;
    stateCell.style.fontWeight = "bold";
    switch (d.state) {
      case "requested":
        stateCell.style.color = "blue"; break;
      case "approved_by_QA":
        stateCell.style.color = "orange"; break;
      case "approved_by_devops":
        stateCell.style.color = "purple"; break;
      case "executed":
        stateCell.style.color = "green"; break;
      case "rejected":
        stateCell.style.color = "red"; break;
      default:
        stateCell.style.color = "black";
    }
    row.appendChild(stateCell);

    // Actions
    const actionCell = document.createElement("td");

    const approveBtn = document.createElement("button");
    approveBtn.textContent = "Approve";
    approveBtn.disabled = d.state === "executed" || d.state === "rejected";
    approveBtn.onclick = () => approveDeployment(d.id);

    const rejectBtn = document.createElement("button");
    rejectBtn.textContent = "Reject";
    rejectBtn.disabled = d.state === "executed" || d.state === "rejected";
    rejectBtn.onclick = () => rejectDeployment(d.id);

    actionCell.appendChild(approveBtn);
    actionCell.appendChild(rejectBtn);
    row.appendChild(actionCell);

    tableBody.appendChild(row);
  });
}

// Create new deployment
async function createDeployment() {
  const nameInput = document.getElementById("deployment-name");
  const name = nameInput.value.trim();
  if (!name) return alert("Enter deployment name");

  await fetch(`${API_URL}/deployments`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name })
  });

  nameInput.value = "";
  fetchDeployments();
}

// Approve deployment
async function approveDeployment(id) {
  await fetch(`${API_URL}/deployments/${id}/approve`, { method: "POST" });
  fetchDeployments();
}

// Reject deployment
async function rejectDeployment(id) {
  await fetch(`${API_URL}/deployments/${id}/reject`, { method: "POST" });
  fetchDeployments();
}

// Initialize
document.getElementById("create-btn").onclick = createDeployment;
fetchDeployments();

