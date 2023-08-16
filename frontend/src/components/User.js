const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.email}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.username}</td>
        </tr>

    )
}

const UsersList = ({users}) => {
    return (
        <table>
            <th>E-mail</th>
            <th>First name</th>
            <th>Last name</th>
            <th>Username</th>
            {users.map((user) => <UserItem user={user}/>)}
        </table>
    )
}

export default UsersList
