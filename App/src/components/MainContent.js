import React, {useState} from 'react';
import { makeStyles } from '@material-ui/core/styles';
import axios from 'axios';
import { TextField, Typography, Button, Box } from '@material-ui/core';

const useStyles = makeStyles(theme => ({
  toolbar: theme.mixins.toolbar,
  title: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.default,
    padding: theme.spacing(3),
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
  },
  fullWidth: {
    width: '100%',
  },
}));

function MainContent() {
  const classes = useStyles();
  const [text, setText] = useState('');
  const api = 'https://mojb7hz560.execute-api.us-east-1.amazonaws.com/lbs-app';

  let [responseData, setResponseData] = React.useState('')

  const handleSubmit = (e) => {
      e.preventDefault()

      if(text){
          console.log(text);

          axios
          .post(api, text)
          .then((response) => {
            console.log(response);
            setResponseData(response.data);
          })
          .catch((error) => {
            console.log(error);
          });
      }
      
  }
  return (
    <main className={classes.fullWidth}>
      <div className={classes.toolbar} />
      <div className={classes.title}>
        <Typography variant='h6'>Title</Typography>
      </div>
      <div>
      <div  className={classes.content}>
            <Typography>
                Enter Paradigm Underneath: 
            </Typography>
            <br />
            <form autoComplete='off' onSubmit ={handleSubmit}>
                <TextField 
                label = "Paradigm Here:"
                variant = 'outlined'
                fullWidth
                onChange={(e) => setText(e.target.value)}
                />
                
                <Button 
                    onClick={handleSubmit}
                    variant = 'contained'
                > Submit </Button>
            </form>
             <Box component="span" sx={{ display: 'block' }}> The judge is: {responseData}</Box> 
        </div>
      </div>
    </main>
  );
}

export default MainContent;