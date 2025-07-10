const express=require('express');
const app=express();

app.use(express.json()); // Add this line to parse JSON bodies


app.get('/',(req,res)=>{
    res.send('This is my project!');
})

app.post('/generate',(req,res)=>{
    // Here you would handle the generation logic
   const text=req.body.text; 
    
})


app.listen(3000,()=>{
    console.log('Server is running on port 3000');
}   );
