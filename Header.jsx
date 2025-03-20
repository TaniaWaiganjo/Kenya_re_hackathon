
const Header = () => {
  return (
    <header className="bg-gray-100 text-navy shadow-[0px_10px_10px_rgba(0,0,0,0.2)] mb-4">
      <div className="container mx-auto flex items-center justify-between h-24 px-8 relative">
        {/* Logo on the far left */}
        <a href="/" className="flex items-center absolute left-8">
          <img className="h-16" src="/logo_resized.png" alt="Logo" />
        </a>

        {/* Centered PI Underwriting text */}
        <h1 className="text-3xl font-serif mx-auto">Personal Indemnity Underwriter</h1>
      </div>
    </header>
  );
};

export default Header;
