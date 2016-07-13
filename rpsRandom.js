function rps(item1, item2) {

    function choose() {
	choice = Math.ceil(Math.random() * 3)
	//console.log(choice);
	if (choice === 1) { return 'Rock!'; } 
	else if (choice === 2) { return 'Paper!'; }
	else /*if (choice === 3)*/ { return 'Scissors!'; }
    }

    item1choice = choose();
    item2choice = choose();
    //console.log(item1 + ': ' + item1choice + ' vs. ' + 
    //		item2 + ': ' + item2choice);
    battle = item1choice + item2choice;

    if (item1choice == item2choice) {
	return rps(item1,item2);
    } else if (battle === 'Rock!Scissors!') {
	//console.log('Rock crushes Scissors!');
	return item1;
    } else if (battle === 'Scissors!Paper!') {
	//console.log('Scissors bisect Paper!');
	return item1;
    } else if (battle === 'Paper!Rock!') {
	//console.log('Paper chokes Rock!');
	return item1;
    } else if (battle === 'Rock!Paper!') {
	//console.log('Rock gets choked by Paper!');
	return item2;
    } else if (battle === 'Paper!Scissors!') {
	//console.log('Paper gets bisected by Scissors!');
	return item2;
    } else /*if (battle === 'Scissors!Rock!')*/ {
	//console.log('Scissors get crushed by Rock!');
	return item2;
    }
}

function rpsSelect(theList) {
    var theChosen = theList,
	end = theChosen.length,
	chop = Math.ceil(end / 2),
	winner;
    //always selects else statement
    while (theChosen.length > 1) {
	winner = rps('0','1');
	if (winner === '1') { theChosen = theChosen.slice(chop,end); }
	else { TheChosen = theChosen.slice(0,chop); }  
    }
    return theChosen
}

console.log(rps('Chuck Norris','Mr.T'));
console.log(rpsSelect(['Coke','Pepsi']));
