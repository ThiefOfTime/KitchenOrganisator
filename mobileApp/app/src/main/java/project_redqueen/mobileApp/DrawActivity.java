package project_redqueen.mobileApp;

import android.bluetooth.BluetoothManager;
import android.bluetooth.BluetoothSocket;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
// bluetooth
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;

import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.support.design.widget.FloatingActionButton;
import android.telecom.ConnectionService;
import android.view.View;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.io.*;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.*;
import java.util.UUID;

public class DrawActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {
    BufferedWriter is = null;
    OutputStream out;
    InputStream in;
    // bluetooth devices
    private BluetoothDevice mmDevice;
    public static BluetoothSocket mmSocket = null;
    private BluetoothAdapter mBluetoothAdapter = null;
    private Thread mConnectedThread;
    private Handler h1;

    public class InputThread implements Runnable {
        private Handler h2;
        private final BluetoothSocket mmSocket;
        private final InputStream mmInStream;
        public InputThread(BluetoothSocket socket, InputStream in, Handler h) {
            this.h2 = h;
            this.mmSocket = socket;
            this.mmInStream = in;
        }

        @Override
        public void run() {
            byte[] buffer = new byte[1024];  // buffer store for the stream
            int bytes; // bytes returned from read()

            // Keep listening to the InputStream until an exception occurs
            while (true) {
                try {
                    // Read from the InputStream
                    bytes = mmInStream.read(buffer);
                    String text = new String(buffer, 0, bytes);
                    Message m = Message.obtain(); //get null message
                    Bundle b = new Bundle();
                    b.putString("uud", text);
                    m.setData(b);
                    //use the handler to send message
                    h2.sendMessage(m);
                    // Send the obtained bytes to the UI activity
                    // mHandler.obtainMessage(MESSAGE_READ, bytes, -1, buffer)
                    //      .sendToTarget();
                } catch (IOException e) {
                    break;
                }
            }
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_draw);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                EditText responseText = (EditText) findViewById(R.id.responseText);
                EditText requestText = (EditText) findViewById(R.id.request_text);
                String Text = requestText.getText().toString();
                final int BUFFER_SIZE = 1024;
                byte[] buffer = new byte[BUFFER_SIZE];
                int bytes = 0;
                try{
                    if(mmSocket.isConnected()){
                        boolean recipes_b = Text.contains("Rezepte") || Text.contains("rezepte") || Text.contains("recipes");
                        boolean show_b = Text.contains("zeige") || Text.contains("liste") || Text.contains("Liste") || Text.contains("alle")
                                || Text.contains("Alle") || Text.contains("all")|| Text.contains("All") || Text.contains("list");
                        if(recipes_b && show_b){
                            // ignore for now
                            Intent intent = new Intent(DrawActivity.this, ReceiptActivity.class);
                            startActivity(intent);
                        }
                        byte[] bffr = Text.getBytes();
                        out.write(bffr);
                        // bytes = in.read(buffer, bytes, BUFFER_SIZE - bytes);
                        // String text = new String(buffer, 0, bytes);
                        // responseText.setText(text);
                        // Toast.makeText(DrawActivity.this, text, Toast.LENGTH_LONG).show();
                    }
                    else{
                        throw new IOException("The device is not connected, please connect to the Hive!");
                    }
                }
                catch(IOException e){
                    //Toast.makeText(this, "damn", Toast.LENGTH_LONG).show();
                    try {
                        mmSocket.close();
                    }catch(IOException f){

                    }
                    Toast.makeText(DrawActivity.this, "Please connect to the Hive", Toast.LENGTH_LONG).show();
                }
                // responseText.setText("Wuhuuuuuu");
            }
        });

        h1 = new Handler(Looper.getMainLooper()) {
            @Override
            public void handleMessage(Message text) {
                EditText responseText = (EditText) findViewById(R.id.responseText);
                responseText.setText(text.getData().getString("uud"));
            }
        };

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.addDrawerListener(toggle);
        toggle.syncState();
        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);

        IntentFilter filter = new IntentFilter(BluetoothDevice.ACTION_FOUND);
        // enabling the bluetooth adapter
        /*if (!mBluetoothAdapter.isEnabled()) {
            Intent enableIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
            startActivityForResult(enableIntent, 1);
        }*/
        // adding bluetooth adapter
        mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
        String status;
        if (!mBluetoothAdapter.isEnabled()) {
            Toast.makeText(this, "Bluetooth is not available", Toast.LENGTH_LONG).show();
            finish();
            return;
        }else{
            String mydeviceaddress = mBluetoothAdapter.getAddress();
            String mydevicename = mBluetoothAdapter.getName();
            status = mydevicename + " : " + mydeviceaddress;
            Toast.makeText(this, status, Toast.LENGTH_LONG).show();
        }
    }


    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.draw, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_camera) {
            // Handle the camera action
        } else if (id == R.id.nav_gallery) {
            if(mmSocket == null || !mmSocket.isConnected()) {
                UUID uuid = UUID.fromString("6ba7b811-9dad-11d1-80b4-00c04fd430c8");
                try {
                    mmDevice = mBluetoothAdapter.getRemoteDevice("30:3A:64:4A:1C:52");
                    mmSocket = mmDevice.createRfcommSocketToServiceRecord(uuid);
                    mmSocket.connect();
                    Toast.makeText(DrawActivity.this, "test", Toast.LENGTH_LONG).show();
                    out = mmSocket.getOutputStream();
                    in = mmSocket.getInputStream();
                    mConnectedThread = new Thread(new InputThread(mmSocket, in, h1));
                    mConnectedThread.start();

                } catch (IOException e) {
                    try {
                        Class<?> clazz = mBluetoothAdapter.getRemoteDevice("30:3A:64:4A:1C:52").getClass();
                        Class<?>[] paramTypes = new Class<?>[] {Integer.TYPE};

                        Method m = clazz.getMethod("createRfcommSocket", paramTypes);
                        Object[] params = new Object[] {Integer.valueOf(1)};
                        mmSocket = (BluetoothSocket) m.invoke(mBluetoothAdapter.getRemoteDevice("30:3A:64:4A:1C:52"), params);
                        mmSocket.connect();
                        Toast.makeText(DrawActivity.this, "test1", Toast.LENGTH_LONG).show();
                        out = mmSocket.getOutputStream();
                        in = mmSocket.getInputStream();
                        mConnectedThread = new Thread(new InputThread(mmSocket, in, h1));
                        mConnectedThread.start();
                    } catch (IOException f) {

                    }
                    catch (NoSuchMethodException g){

                    }
                    catch(IllegalAccessException h){

                    }
                    catch(InvocationTargetException i){

                    }
                }
            }
            else{
                try {
                    String exit = ":quit";
                    out.write(exit.getBytes());
                    mmSocket.close();
                    mmDevice = null;
                }catch(IOException g){

                }

            }


        } else if (id == R.id.nav_slideshow) {

        } else if (id == R.id.nav_manage) {

        } else if (id == R.id.nav_share) {

        } else if (id == R.id.nav_send) {

        }

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }
}
