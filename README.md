The project is a mix of ajax and python to load the script on a SPA.

The functions used are through javascript with the ability to be calling different templated pages with in the file flders as needed. 

$(document).ready(function(){
    $("button").click(function(){
       $.get("/contact", function(data, status){
		$("#show").load("/contact");
        });
    });
});

Is an example of the code used to call functions and pull them.


I had a back button working however it loaded the footer and header twice in the SPA and left me with no option but to remove the back button options.

The database wouldn't work for me as I was unfirmiliar with couchDB and tried to learn it enough to be able to use the couch DB with in the SPA however I couldn't get it to work and so again choose to remavoe it, The code i used for this was the code that we got from our lecturer and tried to incorporate into the project but in the end could not.
