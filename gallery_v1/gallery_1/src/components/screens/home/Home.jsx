import styles from './Home.module.css'



function Home() {
     
    return (
      <div>
        <h1>
          Catalog car
        </h1>
        <div>
            <div className={styles.item}>
                <div className={styles.image} style={
                    {
                        backgroundImage:'url(/1.jpg)',
                    }
                }/>
                <div className={styles.info}>

                    <h2>Car1</h2>
                    <p>$100 000</p>
                    <button>Read more</button>
                </div>
                
            </div>
        </div>
      </div>
    )
  }
  
  export default Home
  