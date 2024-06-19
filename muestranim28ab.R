library("multimode")
library("distr")

mix= UnivarMixingDistribution(Norm(mean=0.85,sd=0.35),Norm(mean=2,sd=0.3),
                              Norm(mean=3.3,sd=0.29),
                              mixCoeff = c(0.52,0.23,0.25))
n=800
rmix= r(mix)
dmix=d(mix)
set.seed(10)
muestra=rmix(n)
rejilla=seq(-2,7,0.001)
plot(rejilla,dmix(rejilla),type="l")
lines(density(muestra), ylim = c(0,0.6))
#lines(rejilla,dmix(rejilla),type="l")
texto = paste(muestra, collapse = ",")
writeLines(texto, "datosanimp1.txt")


#EJECUTAR SI SE QUIEREN LAS VENTANAS. NO COMPENSA SI SOLO ESTÁS PROBANDO FORMAS DE MIXTURA
h=rep(0,6)#tras el for esto será el vector de ventanas criticas
for (i in 1:6){
  h[i]=bw.crit(muestra,mod0=i)
}
texto = paste(h, collapse = ",")
writeLines(texto, "datosanimh.txt")


# if (a == 0) {
#   print("Zero division not allowed")
#   stop()
# }
#Fragmento para calcular las posiciones de h en dicotomía
h
dicotv=rep(0,20)
posi=0.3
for (i in 1:20){
  i
  dicotv[i]=posi
  if (posi>=h[3]){
    posi=posi-0.3/((2)^i)
  }
  else{
    posi=posi+0.3/((2)^i)
  }
}
texto = paste(dicotv, collapse = ",")
writeLines(texto, "datosanimdico.txt")

# suma <- function(x, y) {
#   resultado <- x + y
#   return(resultado)
# }
mixfunden <- function(x){
  resul=0.52*dnorm(x,mean=0.85,sd=0.35)+0.23*dnorm(x,mean=2,sd=0.3)+0.25*dnorm(x,mean=3.3,sd=0.29)
  return(resul)
} 

plot(rejilla,mixfunden(rejilla))
# Norm(mean=0.85,sd=0.35),Norm(mean=2,sd=0.3),
# Norm(mean=3.3,sd=0.29),
# mixCoeff = c(0.52,0.23,0.25)