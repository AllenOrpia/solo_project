
const form = document.querySelector('#searchForm')

// form.addEventListener('submit', async function(e) {
//     e.preventDefault();
//     console.log('Submitted')
//     console.log(form.elements.searchInput.value)
//     const searchInput = form.elements.searchInput.value
//     const res = await axios.get(`http://pokeapi.co/api/v2/berry/${searchInput}/`);
//     const resUrl = res.data.item.url 
//     const res2 = await axios.get(resUrl)
//     console.log(res)
//     console.log(res.data.item.url)
//     console.log(res2)
//     const res2Img = res2.data.sprites.default

//     const div = document.querySelector('#berry-display')
//     const img = document.createElement('IMG');
//     img.src = res2Img
    
    
// })


const gallery = document.querySelector('#gallery-box')
const getBerries = async () => {
    const res = await axios.get('http://pokeapi.co/api/v2/berry?limit=64')
    const results = res.data.results
    console.log(res)
    console.log(results)
    for (let i =0; i < results.length; i++) {

        const res2 = await axios.get(results[i].url)
        const res3 = await axios.get(res2.data.item.url)
        const res3Img = res3.data.sprites.default
      
        const img = document.createElement('IMG')
        const a = document.createElement('A')
        
        a.innerHTML = `${results[i].name}`.toUpperCase()
        a.href = '/berry/' + (results[i].name)
        a.classList.add( 'hover:-translate-y-2','text-center','font-semibold')

        img.src = res3Img
        img.classList.add('w-32','h-32','block')
        a.append(img)
        gallery.append(a)
    

    }

}
getBerries();

const display = document.querySelector('#main-display')
const getBerries2 = async () => {
    const res = await axios.get('http://pokeapi.co/api/v2/berry?limit=4')
    const results = res.data.results
    console.log(res)
    console.log(results)

    for (let i =0; i < results.length; i++){
        const res2 = await axios.get(results[i].url)
        const res3 = await axios.get(res2.data.item.url)
        const res3Img = res3.data.sprites.default

        const img = document.createElement('IMG')
        const p = document.createElement('P')
        const newDiv = document.createElement('DIV')
        newDiv.classList.add('flex', 'flex-col' ,'w-1/3', 'h-1/3', 'bg-gradient-to-tr', 'from-white/70', 'to-white/30', 'rounded-2xl' , 'z-20','justify-center','content-center', 'flex-wrap', 'backdrop-blur-sm')
        p.innerHTML = `${results[i].name}`
        p.classList.add('text-center','text-2xl', 'font-semibold')
        img.src = res3Img
        img.classList.add('w-32','h-32')

        display.append(newDiv)
        newDiv.append(img)
        newDiv.append(p)
    }
}
getBerries2();



const review_container = document.querySelector('#reviews')

const getReviews = async() => {
    
}

const spicy_category = document.querySelector('#spicy') 
const dry_category = document.querySelector('#dry')
const spicy_id = spicy_category.id




const getBerriesByFlavor = async () => {
    const res = await axios.get(`http://pokeapi.co/api/v2/berry-flavor/${spicy_id}`)
    const results = res.data.berries
    console.log(res)
    const spicy_container = document.querySelector('#spicy_container')
    for (let i=0 ; i<results.length; i++ ) {

        const res2 = await axios.get(results[i].berry.url)
        const res3 = await axios.get(res2.data.item.url)
        const res3Img = res3.data.sprites.default
        
        const img = document.createElement('IMG')
        const p = document.createElement('P')
        const newDiv = document.createElement('DIV')
        const a = document.createElement('A')
        
        a.innerHTML = `${results[i].berry.name}`.toUpperCase()
        a.href = '/berry/' + (results[i].berry.name)
        newDiv.classList.add('flex', 'flex-col', 'flex-wrap','w-1/3', 'min-h-full', 'bg-gradient-to-tr', 'from-white/70', 'to-white/30', 'rounded-2xl' , 'z-20','justify-center','content-center', 'flex-wrap', 'backdrop-blur-sm')
        
        img.src = res3Img
        img.classList.add('w-32','h-32')
        
        spicy_container.append(newDiv)
        a.append(img)
        newDiv.append(a)
        
    }
   

}

spicy_category.addEventListener('click', getBerriesByFlavor)
// dry_category.addEventListener('click', getBerriesByFlavor )
// spicy_category.addEventListener('click', getBerriesByFlavor )
// spicy_category.addEventListener('click', getBerriesByFlavor )
// spicy_category.addEventListener('click', getBerriesByFlavor )
