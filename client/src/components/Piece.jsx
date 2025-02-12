import black from "../assets/black.png";
import white from "../assets/white.png";

export default function Piece(props) {
  const color = props.color;

  if (color == "1") {
    return (
      <div className="piece">
        <img src={black} />
      </div>
    );
  } else if (color == "-1") {
    return (
      <div className="piece">
        <img src={white} />
      </div>
    );
  }
}
