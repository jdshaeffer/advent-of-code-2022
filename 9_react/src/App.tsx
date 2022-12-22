import { useEffect, useState } from "react";
import { testInput, input } from '../../9_svelte/src/input';
import "./App.css";

function App() {
  const rowLength = 6;
  const rowLengthArr = [...Array(rowLength)].map(t => '.');

  const [grid, setGrid] = useState(rowLengthArr.map(row => rowLengthArr))

  const changeTile = (tile: string, i: number, j: number) => {
    const newGrid = [...grid]
    newGrid[i][j] = tile
    setGrid(newGrid)
  }

  useEffect(() => {
    let i = 0
    // let head, tail = grid[5][0]
    changeTile('H', 5, 0)
    const intervalId = setInterval(() => {
      // console.log(testInput[i].split(' '))
      

      i++
      if (i === testInput.length) {
        clearInterval(intervalId)
      }
    }, 1000)
  }, [])

  return (
    <div className='App'>
      {grid.map((_, i) => (
        <div key={i} className='row'>
          {grid[i].map((col, j) =>
            <div key={`${i}, ${j}`} className='t'>
              {col}
            </div>
          )}
        </div>
      ))}
    </div>
  );
}

export default App;
