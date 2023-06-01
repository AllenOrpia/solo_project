

const berry_category = document.querySelector('#berry_flavor')
const flavor = berry_category.innerHTML.toLowerCase()


const getBerriesByFlavor = async () => {
    const res = await axios.get(`http://pokeapi.co/api/v2/berry-flavor/${flavor}`)
    const results = res.data.berries
    console.log(res)
    const berry_container = document.querySelector('#berry_flavor_container')
    
    for (let i=0 ; i<results.length; i++ ) {

        const res2 = await axios.get(results[i].berry.url)
        const res3 = await axios.get(res2.data.item.url)
        const res3Img = res3.data.sprites.default
        
        const img = document.createElement('IMG')
        const p = document.createElement('P')
        const h3 = document.createElement('H3')
        const newDiv = document.createElement('DIV')
        const a = document.createElement('A')

        // a.innerHTML = `${results[i].berry.name}`.toUpperCase()
        a.href = '/berry/' + (results[i].berry.name)
        a.classList.add( 'hover:-translate-y-2','text-center','font-semibold')
        newDiv.classList.add('aspect-h-1', 'aspect-w-1', 'w-full', 'overflow-hidden', 'rounded-lg', 'bg-gray-200', 'xl:aspect-h-8', 'xl:aspect-w-7')
        img.classList.add('h-full','w-full', 'object-cover', 'object-center', 'group-hover:opacity-75')
        h3.classList.add('mt-4', 'text-sm', 'text-gray-700')
        p.classList.add('mt-1', 'text-lg', 'font-medium', 'text-gray-900')

        img.src = res3Img
        h3.innerText = results[i].berry.name



        berry_container.append(a)
        a.append(newDiv)
        newDiv.append(img)
        a.append(h3)
        a.append(p)
    }
}

getBerriesByFlavor()