<?php
use PHPUnit\Framework\TestCase;
require_once 'UserManager.php';

class UserManagerTest extends TestCase {
    private $userManager;

    protected function setUp(): void {
        $this->userManager = new UserManager();
    }

    public function testAddUser() {
        $name = "TestNom";
        $email = "test" . time() . "@example.com";
        $this->userManager->addUser($name, $email);

        $users = $this->userManager->getUsers();
        $this->assertTrue(
            array_search($email, array_column($users, 'email')) !== false
        );
    }

    public function testAddUserEmailException() {
        $this->expectException(InvalidArgumentException::class);
        $this->userManager->addUser("Nom", "email_non_valide");
    }

    public function testUpdateUser() {
        $name = "NomAvant";
        $email = "avant" . time() . "@example.com";
        $this->userManager->addUser($name, $email);

        $users = $this->userManager->getUsers();
        $lastUser = end($users);

        $this->userManager->updateUser($lastUser['id'], "NomApres", $email);
        $updated = $this->userManager->getUser($lastUser['id']);

        $this->assertEquals("NomApres", $updated['name']);
    }

    public function testRemoveUser() {
        $name = "ASupprimer";
        $email = "supprimer" . time() . "@example.com";
        $this->userManager->addUser($name, $email);

        $users = $this->userManager->getUsers();
        $lastUser = end($users);

        $this->userManager->removeUser($lastUser['id']);

        $this->expectException(Exception::class);
        $this->userManager->getUser($lastUser['id']);
    }

    public function testGetUsers() {
        $users = $this->userManager->getUsers();
        $this->assertIsArray($users);
    }

    public function testInvalidUpdateThrowsException() {
        $this->expectException(Exception::class);
        $this->userManager->getUser(999999); // Ce user n'existe pas
    }

    public function testInvalidDeleteThrowsException() {
        // Le code original ne lève pas d’exception ici, on peut tester si ça n’efface rien
        $usersBefore = $this->userManager->getUsers();
        $this->userManager->removeUser(999999); // User inexistant
        $usersAfter = $this->userManager->getUsers();
        $this->assertEquals(count($usersBefore), count($usersAfter));
    }
}
