import React, { Component } from 'react'
import { Button,Header, Image, Menu, Segment, Sidebar, Icon } from 'semantic-ui-react'


class SidebarExampleSidebar extends Component {
    state = { visible: false };

    handleHideClick = () => this.setState({ visible: false });
    handleShowClick = () => this.setState({ visible: true });
    handleSidebarHide = () => this.setState({ visible: false });

    render() {
        const { visible } = this.state;

        return (
            <div>
                <Button.Group>
                    <Button disabled={visible} onClick={this.handleShowClick}>
                        Show sidebar
                    </Button>
                    <Button disabled={!visible} onClick={this.handleHideClick}>
                        Hide sidebar
                    </Button>
                </Button.Group>

                <Sidebar.Pushable as={Segment}>
                    <Sidebar
                        as={Menu}
                        animation='overlay'
                        icon='labeled'
                        inverted
                        onHide={this.handleSidebarHide}
                        vertical
                        visible={visible}
                        width='thin'
                    >
                        <Menu.Item as='a'>
                            <Icon name='home' />
                            Home
                        </Menu.Item>
                        <Menu.Item as='a'>
                            <Icon name='chart line' />
                            Marketing
                        </Menu.Item>
                        <Menu.Item as='a'>
                            <Icon name='calendar alternate outline' />
                            Planning
                        </Menu.Item>
                        <Menu.Item as='a'>
                            <Icon name='download' />
                            Production
                        </Menu.Item>
                        <Menu.Item as='a'>
                            <Icon name='archive' />
                            Warehouse
                        </Menu.Item>
                        <Menu.Item as='a'>
                            <Icon name='folder outline' />
                            Ready Products Warehouse
                        </Menu.Item>
                    </Sidebar>

                    <Sidebar.Pusher>
                        <Segment basic>
                            <Header as='h3'>Application Content</Header>
                            <Image src='https://react.semantic-ui.com/images/wireframe/paragraph.png' />
                        </Segment>
                    </Sidebar.Pusher>
                </Sidebar.Pushable>
            </div>
        )
    }
}

export default SidebarExampleSidebar;