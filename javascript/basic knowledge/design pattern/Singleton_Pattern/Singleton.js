class Singleton {
    static instance = null
    
    static getInstance() {
        if (this.instance === null) {
            this.instance = new Singleton()
        }

        return this.instance
    }
}

const a = Singleton.getInstance()

const b = Singleton.getInstance()

console.log(a === b)