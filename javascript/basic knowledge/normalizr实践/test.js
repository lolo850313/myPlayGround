import { normalize, schema } from 'normalizr'

const originalData = {
    "id": "123",
    "author": {
      "id": "1",
      "name": "Paul"
    },
    "title": "My awesome blog post",
    "comments": [
      {
        "id": "324",
        "commenter": {
          "id": "2",
          "name": "Nicole"
        }
      }
    ]
  }



// Define a users schema
const user = new schema.Entity('users')

// Define your comments schema
const comment = new schema.Entity('comments', {
    comment : user
})

// Define your article
const article = new schema.Entity('article', {
    author : user,
    comments : [comment]
})


const normalizedData = normalize(originalData, article)
console.log(normalizedData)

// {
//   result: "123",
//   entities: {
//     "articles": {
//       "123": {
//         id: "123",
//         author: "1",
//         title: "My awesome blog post",
//         comments: [ "324" ]
//       }
//     },
//     "users": {
//       "1": { "id": "1", "name": "Paul" },
//       "2": { "id": "2", "name": "Nicole" }
//     },
//     "comments": {
//       "324": { id: "324", "commenter": "2" }
//     }
//   }
// }

