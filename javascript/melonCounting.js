
// Our customers are going to buy lots of melons!

"use strict";

const melonsToAdd = ['Ogen', 'Horned Melon', 'Watermelon', 'Casaba',
                 'Sharlyn', 'Xigua', 'Ogen', 'Christmas', 'Christmas',
                 'Christmas', 'Christmas', 'Watermelon', 'Sharlyn', 'Xigua',
                 'Cantaloupe', 'Christmas', 'Watermelon', 'Christmas',
                 'Sharlyn', 'Christmas', 'Cantaloupe', 'Casaba', 'Cantaloupe',
                 'Santa Claus', 'Horned Melon', 'Watermelon', 'Ogen',
                 'Horned Melon', 'Cantaloupe', 'Xigua', 'Horned Melon', 'Sharlyn',
                 'Horned Melon', 'Sharlyn', 'Cantaloupe', 'Christmas',
                 'Horned Melon', 'Horned Melon', 'Horned Melon', 'Xigua', 'Xigua',
                 'Watermelon', 'Cantaloupe', 'Casaba', 'Cantaloupe', 'Casaba',
                 'Watermelon', 'Santa Claus', 'Casaba'];


function countMelons(melons) = (melonsObj) => {
    /**
    *  Take in a list and return a dictionary of # of melons by melon type.
    */

    const melonCounts = {};

    for (const melon of melonsObj) {
        if (melonCounts[melon]) {
            melonCounts[melon] += 1;
        }
        else {
            melonCounts[melon] = 1;
        }
    }

    return melonCounts
}

console.log(countMelons(melonsToAdd))
