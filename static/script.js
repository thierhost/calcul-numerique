function jeu()
        {
        
        var valeur=Number(document.forms["matrice_1"]["matrice_1"]);
        bool=false;
        if(valeur>1 && valeur<=10)
        {
          bool=true;
        }
        if(bool==true)
        {
          return true;
        }else
        {
          alert("La taille de la matrice doit etre comprise entre 1 et 10");
          return false;
        }    
        }

function indice(i,j,colone)
{
    return((i-0)*colone+(j-0))
}

function jeu1()
        {
          alert("Bravo! Vous avez trouver la bonne matrice");
         document.location.href="/";
        }

function jeux()
        {
          alert("Looser! Vous avez choisie la mauvaise matrice !");
         document.location.href="/";
        }
  function jeu2()
        {
          jeux();
        }
          function jeu3()
        {
          jeux();
        }
          function jeu4()
        {
          jeux();
        }
      
   
     
function jeu()
        {
         
          var inputs=new Array();
          //inputs.push(document.getElementById("matrice_1").value)
          
          inputs=(document.forms["matrice_1"])
          var taille=Math.sqrt(inputs.length);
          var ech=new Array()
          var mat=new Array();
          for(var i=0;i<taille;i++)
          {
            for(var j=0;j<taille;j++)
            {
              indice="matricea"+(i).toString()+(j).toString();
              // on recupere les inputs au rang de indice
              ech.push(Number(document.forms["matrice_1"][indice].value));
              //console.log(indice);
            }
            mat.push(ech);
            ech=new Array();
            
          }
         /* 
          mettre sous forme de tableaux
         //var matrice_1=Number(document.forms["matrice_1"]["matrice_1"].value);
          var mat=new Array();
          var ech=new Array()
            for(var i=0;i<4;i++)
            {
              for(var j=0;j<4;j++)
              {
                ech.push(i+j)
              }
              mat.push(ech);
              ech=new Array()
            }
            console.log(mat);
            console.log(mat[3][3]);

            */
            console.log(mat);

        }


