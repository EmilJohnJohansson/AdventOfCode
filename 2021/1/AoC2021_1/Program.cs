// See https://aka.ms/new-console-template for more information
using AoC2021_1;

var sweeper = new Sweeper();
var increases = sweeper.CountPointIncreases();
Console.WriteLine(increases);
var slidingIncreases = sweeper.CountSlidingWindowIncreases();
Console.WriteLine(slidingIncreases);