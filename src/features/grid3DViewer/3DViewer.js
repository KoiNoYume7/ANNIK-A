import * as THREE from "three";
import {useEffect, useRef} from "react";

const ThreeDeeScene = () => {
    const mountRef = useRef(null)

    useEffect(() => {
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)
        camera.position.z = 5;

        const renderer = new THREE.WebGLRenderer()
        renderer.setSize(window.innerWidth, window.innerHeight);
        mountRef.current.appendChild(renderer.domElement)

        // Testing Stuff -> Remove afterwards TODO
        const geometry = new THREE.BoxGeometry();
        const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
        const cube = new THREE.Mesh(geometry, material);
        scene.add(cube);

        const animate = () => {
            requestAnimationFrame(animate);
            cube.rotation.x += 0.01;
            cube.rotation.y += 0.01;
            renderer.render(scene, camera);
        };

        animate()

        return () => {
            mountRef.current.removeChild(renderer.domElement);
            renderer.dispose();
        };

    }, []);

    return (
        <div ref={mountRef} />
    );
}
