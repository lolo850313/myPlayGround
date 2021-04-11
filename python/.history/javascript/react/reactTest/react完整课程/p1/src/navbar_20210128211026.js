const Navbar = () => {
    return ( 
        <nav className="navbar">
            <h1>Do jo Blog</h1>
            <div className="links">
                <a href="/">home</a>
                <a href="/create" style={{ 
                    color : "while"
                }}>New blog</a>
            </div>
        </nav>
     );
}
 
export default Navbar;