const grid = document.getElementById("grid");
const rows = 22; 
const cols = 22;
let cells = [];
let interval = null;

function createGrid() {
  grid.innerHTML = ""; 
  cells = Array.from({ length: rows }, () =>
    Array.from({ length: cols }, () => 0)
  );

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      const cell = document.createElement("div");
      cell.classList.add("cell");
      cell.dataset.row = i;
      cell.dataset.col = j;
      cell.addEventListener("click", () => toggleCell(i, j));
      grid.appendChild(cell);
    }
  }
}

function toggleCell(row, col) {
  cells[row][col] = cells[row][col] === 0 ? 1 : 0;
  renderGrid();
}

function renderGrid() {
  const allCells = document.querySelectorAll(".cell");
  allCells.forEach(cell => {
    const row = cell.dataset.row;
    const col = cell.dataset.col;
    if (cells[row][col] === 1) {
      cell.classList.add("alive");
    } else {
      cell.classList.remove("alive");
    }
  });
}

function countNeighbors(row, col) {
  const directions = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1],          [0, 1],
    [1, -1], [1, 0], [1, 1],
  ];
  let count = 0;
  directions.forEach(([dx, dy]) => {
    const x = row + dx;
    const y = col + dy;
    if (x >= 0 && x < rows && y >= 0 && y < cols && cells[x][y] === 1) {
      count++;
    }
  });
  return count;
}

function nextGeneration() {
  const newCells = Array.from({ length: rows }, () => Array(cols).fill(0));
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      const liveNeighbors = countNeighbors(i, j);
      if (cells[i][j] === 1 && (liveNeighbors === 2 || liveNeighbors === 3)) {
        newCells[i][j] = 1;
      } else if (cells[i][j] === 0 && liveNeighbors === 3) {
        newCells[i][j] = 1;
      }
    }
  }
  cells = newCells;
  renderGrid();
}

function startGame() {
  if (!interval) {
    interval = setInterval(nextGeneration, 500); 
  }
}

function stopGame() {
  clearInterval(interval);
  interval = null;
}

function resetGame() {
  stopGame();
  createGrid();
}
document.getElementById("start").addEventListener("click", startGame);
document.getElementById("stop").addEventListener("click", stopGame);
document.getElementById("reset").addEventListener("click", resetGame);
createGrid();
