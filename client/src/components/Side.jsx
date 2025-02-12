import github from '../assets/github-mark.svg';
export default function Side() {
  return (
    <div className="side">
      <ul className="link-list">
        <li>
          <a href="https://github.com/Shin417/Reversi_App_Python">
            <div className="icon-container">
                <img src={github} alt="Github" />
            </div>
          </a>
        </li>
      </ul>
    </div>
  );
}
