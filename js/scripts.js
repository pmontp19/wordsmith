// Randomly select words from object and place into DOM
var $word = words[Math.floor(Math.random()*words.length)];

var $wordName = $word.word;
var $wordSyllabes = $word.syllabes
var $wordType = $word.wordtype;
var $wordDefinition = $word.definition;
var $wordSynonyms = $word.synonyms;
var $wordEtimology = $word.etimology

$( '.js-word' ).html( $wordSyllabes );
$( '.js-type' ).html( $wordType );
$( '.js-definition' ).html( $wordDefinition);
$( '.js-dict-link' ).attr('href', 'https://dlc.iec.cat/results.asp?txtEntrada=' + $wordName );

if ($wordEtimology === '') {
	$( '.js-synonyms' ).hide();
	$( '.text__synonyms--title').hide();
} else {
	$( '.js-synonyms' ).html( $wordEtimology );
}

var original = $('.js-word').text();
var new_version = original.split('·').join('<span class="interpunct">·</span>');
$('.js-word').html(new_version);


// modify array
function nextVal(arr) {
	firstElm = arr.shift();
	arr.push(firstElm);
	backgroundColorDelta(firstElm);
	return arr;
}

// set background color
function backgroundColorDelta (firstElm) {
	$( 'body' ).css('background-image', 'linear-gradient( 135deg, '+firstElm[0]+' 10%, '+firstElm[1]+' 100%)');
}

if (localStorage.getItem('localColorArr') === null) {
	//set array first time if it doesn't exist
	var colorsArr = coolhue;
	localStorage.setItem('localColorArr', JSON.stringify(colorsArr));
	var localColorArr = JSON.parse(localStorage.getItem('localColorArr'));
} else {
	var localColorArr = JSON.parse(localStorage.getItem('localColorArr'));
	//modify array
	modifiedColors = nextVal(localColorArr);
	// set setLocalStorage = modifiedArray;
	localStorage.setItem('localColorArr', JSON.stringify(modifiedColors));
}
