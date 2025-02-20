async function buscarDados() {
    try {
        // const response = await fetch('https://fakestoreapi.com/products');
        // const dados = await response.json();

        // var div = document.getElementById("product-list");
        
        // dados.forEach(element => {

        //     var conteudo = document.createElement('div');
        //     conteudo.innerHTML = `
        //         <img src="${element.image}" alt="${element.title}">
        //         h3>${element.title}</h3>
        //         <p>${element.price}</p>
        //         <p>${element.description}</p>
        //     `

        //     div.appendChild(conteudo);
        // })

        // const novoProduto = {
        //     title: "Novo Produto",
        //     price: 99.99,
        //     description: "Novo produto criado no front-end",
        //     image: "https://via.placeholder.com/150",
        //     categoria: "Eletrônicos"
        // }

        // var resposta = await fetch('https://fakestoreapi.com/products', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify(novoProduto)
           
        // })

        // console.log(await resposta.json());


      
    } catch (error) {
        
    }
}   

async function API(url, method="GET", body=null, headers={}) {

    try {
        const option = ({
            method,
            body,
            headers: {
                'Content-Type': 'application/json',
                ...headers
            }
        }
        );


        if(body) {
            option.body = JSON.stringify(body)
        }

        const resposta = await fetch(url, option);

        const dados = await resposta.json();
        return dados;
        
    } catch (error) {
        console.log(error);
    }       
}

async function buscarProdutos() {
    const produtos = await API('https://fakestoreapi.com/products',(title, price, description, image, categoria));
    console.log(produtos);
}

buscarProdutos();