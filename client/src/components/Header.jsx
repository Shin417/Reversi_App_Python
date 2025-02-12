import github from '../assets/github-mark.svg'
export default function Header(){
    return(
        <header className="header">
            <h1>Reversi</h1>
            <ul className="links">
                <li>
                    <div>
                        <a href=""><img src={github} alt="GitHub"/></a>
                    </div>
                </li>
            </ul>
        </header>
    );
}