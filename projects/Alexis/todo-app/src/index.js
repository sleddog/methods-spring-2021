import { StrictMode } from "react";
import ReactDOM from "react-dom";

import ToDo from "./ToDo";

const rootElement = document.getElementById("root");
ReactDOM.render(
  <StrictMode>
    <ToDo />
  </StrictMode>,
  rootElement
);
