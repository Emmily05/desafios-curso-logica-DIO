const herois = [
    {nome:"Red", xp:26000},
    {nome:"Blue", xp:10000},
    {nome:"Pokemon", xp:5680},
    {nome:"Serena", xp:3767},
    {nome:"Calem", xp:4821},
    {nome:"Brendan", xp:200},
    {nome:"Lucas", xp:9873}

]

for (let i = 0; i < herois.length; i++) {

let nivel

if (herois[i].xp < 1000) {
    nivel = "ferro"
} else if (herois[i].xp > 1000 && herois[i].xp <= 2000) {
    nivel = "Bronze"
} else if (herois[i].xp > 2000 && herois[i].xp <= 5000) {
    nivel = "Prata"
} else if (herois[i].xp > 5000 && herois[i].xp <= 7000) {
    nivel = "Ouro"
} else if (herois[i].xp > 7000 && herois[i].xp <= 8000) {
    nivel = "Platina"
} else if (herois[i].xp > 8000 && herois[i].xp <= 9000) {
    nivel = "Ascendente"
} else if (herois[i].xp > 9000 && herois[i].xp <= 10000) {
    nivel = "Imortal"
} else if (herois[i].xp >= 10001) {
    nivel = "Radiante"
}

console.log ("O Herói de nome " + herois[i].nome + " está no nível " + nivel)
}