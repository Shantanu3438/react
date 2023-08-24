import { Tile } from "./Tile"
import movie from "./movie.jsx"

export function MovieTile() {

  const tiles = movie.map(item => {
    return (
      <Tile 
        coverImage = {item.coverImg}
        title = {item.title} />
    )
  })

    return (
        <div className="movietile">
            {tiles}
        </div>
    )
}