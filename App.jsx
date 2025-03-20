
import React from "react";
import Header from "./components/Header";
import axios from "axios";

//import FileUpload from "./components/FileUpload";
import Modal from "./components/Modal";
import Summary from "./components/Summary";

const App = () => {
  return (
    <div className="w-full min-h-screen bg-gray-100">
      <Header />
      <Modal />
      <Summary />

    </div>
  );
};

export default App;

