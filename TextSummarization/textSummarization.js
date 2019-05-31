let str = `Terms and Conditions ("Terms")  
==============================

Last updated: April 22, 2019

Please read these Terms and Conditions ("Terms", "Terms and Conditions")
carefully before using the cool.com website (the "Service") operated by
Coolness ("us", "we", or "our").

Your access to and use of the Service is conditioned on your acceptance of and
compliance with these Terms. These Terms apply to all visitors, users and
others who access or use the Service.

By accessing or using the Service you agree to be bound by these Terms. If you
disagree with any part of the terms then you may not access the Service. The
Terms and Conditions agreement for Coolness has been created with the help of
[TermsFeed Terms and Conditions Generator](https://termsfeed.com/terms-
conditions-generator/).

Accounts  
--------

When you create an account with us, you must provide us information that is
accurate, complete, and current at all times. Failure to do so constitutes a
breach of the Terms, which may result in immediate termination of your account
on our Service.

You are responsible for safeguarding the password that you use to access the
Service and for any activities or actions under your password, whether your
password is with our Service or a third-party service.

You agree not to disclose your password to any third party. You must notify us
immediately upon becoming aware of any breach of security or unauthorized use
of your account.

Links To Other Web Sites  
------------------------

Our Service may contain links to third-party web sites or services that are
not owned or controlled by Coolness.

Coolness has no control over, and assumes no responsibility for, the content,
privacy policies, or practices of any third party web sites or services. You
further acknowledge and agree that Coolness shall not be responsible or
liable, directly or indirectly, for any damage or loss caused or alleged to be
caused by or in connection with use of or reliance on any such content, goods
or services available on or through any such web sites or services.

We strongly advise you to read the terms and conditions and privacy policies
of any third-party web sites or services that you visit.

Termination  
-----------

We may terminate or suspend access to our Service immediately, without prior
notice or liability, for any reason whatsoever, including without limitation
if you breach the Terms.

All provisions of the Terms which by their nature should survive termination
shall survive termination, including, without limitation, ownership
provisions, warranty disclaimers, indemnity and limitations of liability.

We may terminate or suspend your account immediately, without prior notice or
liability, for any reason whatsoever, including without limitation if you
breach the Terms.

Upon termination, your right to use the Service will immediately cease. If you
wish to terminate your account, you may simply discontinue using the Service.

All provisions of the Terms which by their nature should survive termination
shall survive termination, including, without limitation, ownership
provisions, warranty disclaimers, indemnity and limitations of liability.

Governing Law  
-------------

These Terms shall be governed and construed in accordance with the laws of
Hong Kong, without regard to its conflict of law provisions.

Our failure to enforce any right or provision of these Terms will not be
considered a waiver of those rights. If any provision of these Terms is held
to be invalid or unenforceable by a court, the remaining provisions of these
Terms will remain in effect. These Terms constitute the entire agreement
between us regarding our Service, and supersede and replace any prior
agreements we might have between us regarding the Service.

Changes  
-------

We reserve the right, at our sole discretion, to modify or replace these Terms
at any time. If a revision is material we will try to provide at least 15 days
notice prior to any new terms taking effect. What constitutes a material
change will be determined at our sole discretion.

By continuing to access or use our Service after those revisions become
effective, you agree to be bound by the revised terms. If you do not agree to
the new terms, please stop using the Service.

Contact Us  
----------

If you have any questions about these Terms, please contact us.
`;
const stopWords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'therefore', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"];
str = str.split("\n").join(" ").split(".");
let arr = str.map(val => {
    let split = val.split(" ");
    return split.map(val => {
        let keep = true;
        stopWords.map(v => {
            if (val.toLowerCase() == v.toLowerCase()) {
                keep = false;
            }
        });
        if (keep) {
            return val;
        }
    });
});
let newArr = [],
    bow = [],
    count = 1;
for (let i = 0; i < arr.length; i++) {
    for (let ii = 0; ii < arr[i].length; ii++) {
        if (arr[i][ii] !== undefined && arr[i][ii] !== "") {
            newArr.push(arr[i][ii].toLowerCase());
        }
    }
}
newArr = newArr.sort((a, b) => {
    return a.localeCompare(b);
});
while (newArr.length) {
    if (newArr[1]) {
        if (newArr[0] == newArr[1]) {
            count++;
        } else {
            bow.push([newArr[0].slice(), JSON.parse(JSON.stringify(count))]);
            count = 1;
        }
    } else {
        bow.push([newArr[0].slice(), JSON.parse(JSON.stringify(count))]);
        count = 1;
    }
    newArr.splice(0, 1);
}
let max = bow[0][1];
for (let i = 0; i < bow.length; i++) {
    if (max < bow[i][1]) {
        max = bow[i][1];
    }
}
bow = bow.map(val => {
    return [val[0], val[1] / max];
});
// Now match all the letters with their values in the actual array.
for (let i = 0; i < str.length; i++) {
    // Going through each sentence...
    let spl = str[i].split(" "),
        add = 0;
    for (let ii = 0; ii < spl.length; ii++) {
        for (let z = 0; z < bow.length; z++) {
            if (bow[z][0] == spl[ii].toLowerCase()) {
                add += bow[z][1];
            }
        }
    }
    str[i] = [str[i], add];
}
console.log(JSON.stringify(str, null, "  "));