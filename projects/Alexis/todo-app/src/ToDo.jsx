import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import ToDoItem from "./ToDoItem";
import { TextField } from "@material-ui/core";
import withStyles from "@material-ui/core/styles/withStyles";
import Image from "./beige.jpg";
import { Divider } from "@material-ui/core";

const useStyles = makeStyles({
  app: {
    backgroundImage: `url(${Image})`,
    backgroundPosition: "center",
    backgroundSize: "cover",
    backgroundRepeat: "no-repeat",
    width: "100%",
    height: window.innerWidth,
    padding: "5% 10%"
  },
  main: {
    width: "80%",
    color: "white"
  },
  title: {
    fontSize: "40px"
  },
  content: {
    width: "75%",
    margin: "10%",
    padding: "10px",
    backgroundColor: "#C39473"
  },
  form: {
    display: "flex",
    flexDirection: "row"
  },
  currentText: {
    marginLeft: "5%"
  },
  topDivider: {
    marginRight: "40%"
  },
  bottomDivider: {
    marginLeft: "40%",
    width: "60%"
  }
});

const CssTextField = withStyles({
  root: {
    "& label.Mui-focused": {
      color: "black"
    },
    "& .MuiInput-underline:after": {
      borderBottomColor: "black"
    },
    width: "60%",
    marginRight: "15px"
  }
})(TextField);

const ToDo = () => {
  const classes = useStyles();
  const [newItem, setNewItem] = useState("");
  const [itemList, setItemList] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (newItem) {
      setItemList((prev) => [...prev, newItem]);
      setNewItem("");
    }
  };

  const ToDoList = ({ list }) => {
    const itemsList = list.map((item) => {
      return <ToDoItem key={item} item={item} />;
    });
    return <div>{itemsList}</div>;
  };

  return (
    <div className={classes.app}>
      <div className={classes.main}>
        <p className={classes.title}>Your ToDo List:</p>
        <Divider className={classes.topDivider} />
        <div className={classes.content}>
          <form onSubmit={handleSubmit} className={classes.form}>
            <CssTextField
              value={newItem}
              onChange={(e) => setNewItem(e.target.value)}
              label="Enter a Task"
            />
            <p className={classes.currentText}>
              Currently {itemList.length}{" "}
              {itemList.length > 1 || !itemList.length ? "items" : "item"} on
              your ToDo list.
            </p>
          </form>
          <ToDoList list={itemList} />
        </div>
        <Divider className={classes.bottomDivider} />
      </div>
    </div>
  );
};
export default ToDo;
