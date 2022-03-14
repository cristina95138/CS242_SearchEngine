const express = require('express');

// recordRoutes is an instance of the express router.
// We use it to define our routes.
// The router will be added as a middleware and will take control of requests starting with path /listings.
const recordRoutes = express.Router();

// This will help us connect to the database
const dbo = require('../db/conn');

function getTermFreqInQuery(searchTerm, query) {
    var count = 0;
    for(let i = 0; i < query.length; i++) {
        if(query[i] == searchTerm) {
            count++;
        }
    }

    return count;
}

// N: size of collection aka number of documents
// n_k: number of documents the word appears in
function getInvDocFreq(N, searchTerm, result) {
    var n_k = 0;

    for(let i = 0; i < result.length; i++) {
        if(result[i]['token'] == searchTerm) {
            var keys = Object.keys(result[i]);
            n_k = keys.length - 2;
            break;
        }
    }

    return Math.log(N / n_k);
}

function getCosineSimilarity(A, B) {
    var dotProduct = 0;
    var mA = 0;
    var mB = 0;

    for(let i = 0; i < A.length; i++) {
        dotProduct += (A[i] * B[i]);
        mA += (A[i] * A[i]);
        mB += (B[i] * B[i]);
    }

    mA = Math.sqrt(mA);
    mB = Math.sqrt(mB);

    return (dotProduct) / ((mA) * (mB));
}

// This section will help you get a list of all the records.
recordRoutes.route('/search').get(async function (_req, res) {
  const dbConnect = dbo.getDb();

  dbConnect
    .collection('counts')
    .find({})
    .toArray(function (err, result) {
        // console.log(result[0]['token']);
        const query = _req.query.query.split(" ");
        var docArrays = [];
        var queryArray = [];
        var docSums = [];

        for(let i = 0; i < 6; i++) {
            docSums.push(0);
        }
        // Calculate docSums
        for(let i = 0; i < result.length; i++) {
            var keys = Object.keys(result[i]);
            for(let j = 0; j < keys.length - 2; j++) {
                docSums[keys[j]-1] += parseInt(result[i][keys[j]], 10);
            }
        }

        // For every term in result:
        //  Calculte the tf * invDocFreq for the given document/query
        for(let i = 0; i < result.length; i++) {
            var docSum = query.length;
            var f_ik = getTermFreqInQuery(result[i]["token"], query);
            var tf = f_ik / docSum;
            var invDocFreq = getInvDocFreq(6, result[i]["token"], result);
            if(isNaN(tf * invDocFreq)) {
                queryArray.push(0);
            }
            else {
                queryArray.push(tf * invDocFreq);
            }
        }
        console.log(queryArray);

        for(let i = 1; i <= 6; i++) {
            var termFreqs = [];
            for(let j = 0; j < result.length; j++) {
                // Frequency of a word in a single document i
                var f_ik = result[j][i];
                // Sum of all words in a single document i
                var docSum = docSums[i-1];
                var tf = f_ik / docSum;
                var invDocFreq = getInvDocFreq(6, result[j]["token"], result);
                var tfIdf = tf * invDocFreq;
                if(isNaN(tfIdf) || tfIdf == Infinity) {
                    termFreqs.push(0);
                }
                else {
                    termFreqs.push(tf * invDocFreq);
                }
            }
            docArrays.push(termFreqs);
        }

        var maxCosineVal = 0;
        var docId = 1;
        for(let i = 0; i < docArrays.length; i++) {
            var currCosineVal = getCosineSimilarity(queryArray, docArrays[i]);
            console.log(currCosineVal);
            if(currCosineVal > maxCosineVal) {
                maxCosineVal = currCosineVal;
                docId = i + 1;
            }
        }

        if (err) {
            res.status(400).send('Error fetching listings!');
        } else {
            res.json(docId);
        }
    });
});

// This section will help you create a new record.
// recordRoutes.route('/listings/recordSwipe').post(function (req, res) {
//   const dbConnect = dbo.getDb();
//   const matchDocument = {
//     listing_id: req.body.id,
//     last_modified: new Date(),
//     session_id: req.body.session_id,
//     direction: req.body.direction,
//   };

//   dbConnect
//     .collection('matches')
//     .insertOne(matchDocument, function (err, result) {
//       if (err) {
//         res.status(400).send('Error inserting matches!');
//       } else {
//         console.log(`Added a new match with id ${result.insertedId}`);
//         res.status(204).send();
//       }
//     });
// });

// This section will help you update a record by id.
// recordRoutes.route('/listings/updateLike').post(function (req, res) {
//   const dbConnect = dbo.getDb();
//   const listingQuery = { _id: req.body.id };
//   const updates = {
//     $inc: {
//       likes: 1,
//     },
//   };

//   dbConnect
//     .collection('listingsAndReviews')
//     .updateOne(listingQuery, updates, function (err, _result) {
//       if (err) {
//         res
//           .status(400)
//           .send(`Error updating likes on listing with id ${listingQuery.id}!`);
//       } else {
//         console.log('1 document updated');
//       }
//     });
// });

// This section will help you delete a record.
// recordRoutes.route('/listings/delete/:id').delete((req, res) => {
//   const dbConnect = dbo.getDb();
//   const listingQuery = { listing_id: req.body.id };

//   dbConnect
//     .collection('listingsAndReviews')
//     .deleteOne(listingQuery, function (err, _result) {
//       if (err) {
//         res
//           .status(400)
//           .send(`Error deleting listing with id ${listingQuery.listing_id}!`);
//       } else {
//         console.log('1 document deleted');
//       }
//     });
// });

module.exports = recordRoutes;