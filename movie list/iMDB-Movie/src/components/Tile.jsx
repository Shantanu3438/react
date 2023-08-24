export function Tile(props) {
    return(
        <div className="tile">
            <img src={props.coverImage} className="tile--poster"/>
            <p className="tile--title">{props.title}</p>
        </div>
    )
}