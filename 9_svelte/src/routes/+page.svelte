<script lang="ts">
  import { testInput, input } from '../input';

  const rowLength = 300;
  const rowLengthArr = [...Array(rowLength)].map((t) => '.');
  let grid = rowLengthArr.map((row) => [...rowLengthArr]);
  let i = 0;
  let n = 0;
  let count = 0;

  // starting position
  const startingPosition = [50, 50];
  let h = startingPosition;
  let t = startingPosition;
  let prevH = h;
  let prevT = t;

  const intervalId = setInterval(() => {
    const [dir, num] = input[i].split(' ');

    grid[prevH[0]][prevH[1]] = grid[prevH[0]][prevH[1]] === 'H#' ? '#' : '.';
    grid[prevT[0]][prevT[1]] = '#';
    grid[h[0]][h[1]] = grid[h[0]][h[1]] === '#' ? 'H#' : 'H';
    grid[t[0]][t[1]] = 'T';

    prevH = h;
    prevT = t;
    if (dir === 'R') {
      h = [h[0], h[1] + 1];
    } else if (dir === 'L') {
      h = [h[0], h[1] - 1];
    } else if (dir === 'U') {
      h = [h[0] - 1, h[1]];
    } else if (dir === 'D') {
      h = [h[0] + 1, h[1]];
    }

    // if they're touching, don't move t
    const touching =
      (t[0] === h[0] + 1 && t[1] === h[1] - 1) || // ne
      (t[0] === h[0] + 1 && t[1] === h[1] + 1) || // nw
      (t[0] === h[0] - 1 && t[1] === h[1] + 1) || // sw
      (t[0] === h[0] - 1 && t[1] === h[1] - 1) || // se
      (t[0] === h[0] && t[1] === h[1] - 1) || // e
      (t[0] === h[0] && t[1] === h[1] + 1) || // w
      (t[0] === h[0] + 1 && t[1] === h[1]) || // n
      (t[0] === h[0] - 1 && t[1] === h[1]); // s

    if (!touching) {
      t = prevH;
    }

    ///////////////////////////////////////////////

    n++;
    if (n === +num) {
      n = 0;
      i++;
    }
    if (i === input.length) {
      clearInterval(intervalId);
      for (const [i, _] of grid.entries()) {
        for (const curr of grid[i]) {
          if (curr.includes('#')) {
            count++;
          }
        }
      }
    }
  }, 5);
</script>

<main>
  <div class="app">
    {#each grid as _, i}
      <div class="row">
        {#each grid[i] as col, j}
          <div class="t">
            {col}
          </div>
        {/each}
      </div>
    {/each}
    <div class="ans">
      answer: {count}
    </div>
  </div>
</main>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS',
      sans-serif;
  }

  :root {
    --tile-size: 20px;
  }

  .app {
    text-align: center;
    background-color: #282c34;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    font-size: 15px;
  }

  .ans {
    display: flex;
    flex-direction: row;
    color: blanchedalmond;
  }

  .t {
    background-color: blanchedalmond;
    min-width: var(--tile-size);
    padding-bottom: var(--tile-size);
    height: 0;
    color: black;
  }

  .row {
    display: flex;
    flex-direction: row;
  }
</style>
