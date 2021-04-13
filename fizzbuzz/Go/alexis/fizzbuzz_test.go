package main

import (
	"testing"
)

func TestFizz( t *testing.T )  {
	result := fizzbuzz(3)
	if result != "fizz" {
		t.Errorf("testFizz failed, expected: fizz, got %v", result)
	} else {
		t.Logf("testFizz success, expected: fizz, got %v", result)
	}
}

func TestBuzz( t *testing.T )  {
	result := fizzbuzz(5)
	if result != "buzz" {
		t.Errorf("testFizz failed, expected: buzz, got %v", result)
	} else {
		t.Logf("testFizz success, expected: buzz, got %v", result)
	}
}

func TestPing( t *testing.T )  {
	result := fizzbuzz(7)
	if result != "ping" {
		t.Errorf("testFizz failed, expected: ping, got %v", result)
	} else {
		t.Logf("testFizz success, expected: ping, got %v", result)
	}
}

func TestPong( t *testing.T )  {
	result := fizzbuzz(11)
	if result != "pong" {
		t.Errorf("testFizz failed, expected: pong, got %v", result)
	} else {
		t.Logf("testFizz success, expected: pong, got %v", result)
	}
}

func TestFizzBuzz( t *testing.T )  {
	result := fizzbuzz(15)
	if result != "fizzbuzz" {
		t.Errorf("testFizz failed, expected: fizzbuzz, got %v", result)
	} else {
		t.Logf("testFizz success, expected: fizzbuzz, got %v", result)
	}
}

func TestFizzPing( t *testing.T )  {
	result := fizzbuzz(21)
	if result != "fizzping" {
		t.Errorf("testFizz failed, expected: fizzping, got %v", result)
	} else {
		t.Logf("testFizz success, expected: fizzping, got %v", result)
	}
}

func TestFizzPong( t *testing.T )  {
	result := fizzbuzz(33)
	if result != "fizzpong" {
		t.Errorf("testFizz failed, expected: fizzpong, got %v", result)
	} else {
		t.Logf("testFizz success, expected: fizzpong, got %v", result)
	}
}

func TestFizzBuzzPing( t *testing.T )  {
	result := fizzbuzz(105)
	if result != "fizzbuzzping" {
		t.Errorf("testFizz failed, expected: fizzbuzzping, got %v", result)
	} else {
		t.Logf("testFizz success, expected: fizzbuzzping, got %v", result)
	}
}

func TestFizzBuzzPong( t *testing.T )  {
	result := fizzbuzz(165)
	if result != "fizzbuzzpong" {
		t.Errorf("testFizz failed, expected: fizzbuzzpong, got %v", result)
	} else {
		t.Logf("testFizz success, expected: fizzbuzzpong, got %v", result)
	}
}

func TestFizzBuzzPingPong( t *testing.T )  {
	result := fizzbuzz(1155)
	if result != "fizzbuzzpingpong" {
		t.Errorf("testFizz failed, expected: fizzbuzzpingpong, got %v", result)
	} else {
		t.Logf("testFizz success, expected: fizzbuzzpingpong, got %v", result)
	}
}

func TestBuzzPing( t *testing.T )  {
	result := fizzbuzz(35)
	if result != "buzzping" {
		t.Errorf("testFizz failed, expected: buzzping, got %v", result)
	} else {
		t.Logf("testFizz success, expected: buzzping, got %v", result)
	}
}

func TestBuzzPong( t *testing.T )  {
	result := fizzbuzz(55)
	if result != "buzzpong" {
		t.Errorf("testFizz failed, expected: buzzpong, got %v", result)
	} else {
		t.Logf("testFizz success, expected: buzzpong, got %v", result)
	}
}

func TestBuzzPingPong( t *testing.T )  {
	result := fizzbuzz(385)
	if result != "buzzpingpong" {
		t.Errorf("testFizz failed, expected: buzzpingpong, got %v", result)
	} else {
		t.Logf("testFizz success, expected: buzzpingpong, got %v", result)
	}
}

func TestPingPong( t *testing.T )  {
	result := fizzbuzz(77)
	if result != "pingpong" {
		t.Errorf("testFizz failed, expected: pingpong, got %v", result)
	} else {
		t.Logf("testFizz success, expected: pingpong, got %v", result)
	}
}
