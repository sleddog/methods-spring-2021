import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import { ListItem } from "@material-ui/core";
import { Checkbox } from "@material-ui/core";
import Grid from "@material-ui/core/Grid";

const useStyles = makeStyles({
  itemHolder: {
    display: "flex",
    flexDirection: "row"
  },
  checkBoxRow: {
    display: "flex",
    flexDirection: "row"
  }
});

const ToDoItem = ({ item }) => {
  const classes = useStyles();
  return (
    <ListItem button value={item} className={classes.itemHolder}>
      <Grid container spacing={4}>
        <Grid item xs={6} className={classes.checkBoxRow}>
          <Checkbox
            color="default"
            inputProps={{ "aria-label": "checkbox with default color" }}
          />
          <p>{item}</p>
        </Grid>
      </Grid>
    </ListItem>
  );
};
export default ToDoItem;
