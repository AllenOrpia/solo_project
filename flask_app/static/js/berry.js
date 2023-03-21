

let berry = {
//     id :document.querySelector('#berry_id').value,
    name: document.querySelector('#berry_name').value
}


const berry_box = document.querySelector('#berry-container')

// const getBerry = async () => {

//         const res = await axios.get(`http://pokeapi.co/api/v2/berry/${berry.id}`)
//         const res2 = await axios.get(res.data.item.url)
//         const res2Effect = res2.data.effect_entries[0].effect
//         const res2Img = res2.data.sprites.default
//         console.log(res)
        
//         const img = document.createElement('IMG')
//         img.src =  res2Img
//         img.classList.add('w-32', 'h-32')
//         berry_box.append(img)
    
//         const h1 = document.createElement('H1')
//         h1.innerHTML = res.data.item.name
//         h1.classList.add('text-3xl', 'font-bold')
//         berry_box.append(h1)

//         const p = document.createElement('P')
//         p.innerHTML = res2Effect
//         berry_box.append(p)
// }

const getBerryByName = async () => {
        const nameRes = await axios.get(`http://pokeapi.co/api/v2/berry/${berry.name}`)
        const nameRes2 = await axios.get(nameRes.data.item.url)
        const nameRes2Effect = nameRes2.data.effect_entries[0].effect
        const nameRes2Img = nameRes2.data.sprites.default
        console.log(nameRes)
        console.log(nameRes2)
    
        const img = document.createElement('IMG')
        img.src =  nameRes2Img
        img.classList.add('w-32', 'h-32')
        berry_box.append(img)
    
        const h1 = document.createElement('H1')
        h1.innerHTML = nameRes.data.item.name
        h1.classList.add('text-3xl', 'font-bold')
        berry_box.append(h1)

        const p = document.createElement('P')
        p.innerHTML = nameRes2Effect
        berry_box.append(p)
}
   

// getBerry()
getBerryByName()